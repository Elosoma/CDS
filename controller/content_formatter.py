'''Documento de gestión de formato, extrae datos de la db y los maqueta para mostrarlos en la interfaz gráfica.'''
from model.api_2014 import DnDAPI

def format_class_levels(levels: list[dict]) -> str:
    lines = []
    api = DnDAPI()

    for lvl in levels:
        lines.append(f"LVL {lvl['level']}")
        lines.append("_" * 20)

        # Features
        features = lvl.get("features", [])
        if features:
            lines.append("Features:")
            for f in features:
                lines.append(f"  - {f['name']}")
                feature:dict = api.get_feature(f["index"])
                for des in feature.get('desc'):
                    lines.append(f"  {des}")
                lines.append("")

        lines.append("")  # separación entre niveles

    return "\n".join(lines)

def format_class(data: dict) -> str:
    lines = []
    api = DnDAPI()

    # TITULO : Nombre de la clase, puntos de golpe y tiradas de salvación seguido de un separador estético.
    lines.append(data["name"].upper())
    lines.append("_" * 20)
    lines.append("")

    lines.append(f"Hit Die: d{data.get('hit_die')}")
    lines.append("Saving Throws:")
    for s in data.get("saving_throws", []):
        lines.append(f"  - {s['name']}")
    lines.append("")

    # CUERPO : Elecciones de ventaja y ventajas de clase, equipo y multiclase.
    for c in data.get("proficiency_choices", []):
        desc = c.get("desc", "")
    lines.append(f"Proficiency Choices:\n{desc}")
    lines.append("")
    
    lines.append("Proficiencies:")
    for p in data.get("proficiencies", []):
        lines.append(f"  - {p['name']}")
    lines.append("")

    lines.append("Equipment")
    for e in data.get("starting_equipment"):
        lines.append(f"  -{e['quantity']} {e['equipment']['name']}")

    for e in data.get("starting_equipment_options"):
        lines.append(f"  -{e['desc']}")
    lines.append("")

    # Multiclase
    multi = data.get("multi_classing")
    if multi:
        lines.append("Multiclass:")
        lines.append("  Prerequisites:")

        for req in multi.get("prerequisites", []):
            ability = req["ability_score"]["name"]
            score = req["minimum_score"]
            lines.append(f"    - {ability} ≥ {score}")

        lines.append("")
        lines.append("  Multiclass proficiencies:")

        for pro in multi.get("proficiencies", []):
            lines.append(f"    - {pro['name']}")

        lines.append("")

    # NIVELES : 
    lines.append(format_class_levels(api.get_class_levels(data.get("index"))))

    lines.append("_" * 20)
    lines.append("\n")
    lines.append("Subclasess")
    lines.append("")

    for sub in data.get('subclasses'):
        subclass:dict = api.get_subclass(sub['index'])

        lines.append(sub['name'])
        for des in subclass.get('desc'):
            lines.append(des)
        lines.append("")
        lines.append(format_class_levels(api.get_subclass_levels(sub['index'])))


    return "\n".join(lines)



# <---> <---> <---> <---> <---> <--->



def format_race(data: dict) -> str:
    lines = []
    api = DnDAPI()

    # TITULO : Nombre de la raza seguido de un separador estético.
    lines.append(data["name"].upper())
    lines.append("_" * 20)
    lines.append("")

    # CUERPO : Velocidad, bonus raciales y descripción (alineamiento, edad, tamaño y lengua).
    lines.append(f"Speed: {data.get('speed')}")

    lines.append(f"Ability Bonuses:")
    for ab in data.get("ability_bonuses", []):
        lines.append(f"  - {ab['ability_score']['name']}: +{ab['bonus']}")
    lines.append("")

    lines.append(f"Description:\n{data.get('alignment')}{data.get('age')}{data.get('size_description')}{data.get('language_desc')}")
    lines.append("")
    lines.append("_" * 20)

    # OTROS : Listas de rasgos y subrazas.
    if data.get("traits") != []:
        lines.append("Traits:")
        lines.append("")
        for t in data.get("traits", []):
            lines.append(f"  -{t['name'].upper()}:")
            desc:dict = api.get_trait(t['index'])
            for d in desc.get("desc", []):
                lines.append(f"  {d}")
            lines.append("")

    if data.get("subraces") != []:
        lines.append("_" * 20)
        lines.append("Subraces:")
        lines.append("")

        # Cada subraza incluye sus caracteristicas y/o modificadores.
        for s in data.get("subraces", []):
            subr:dict = api.get_subrace(s['index'])

            # Nombre y descripción.
            lines.append(f"-{s['name'].upper()}:")

            lines.append(f"{subr.get('desc')}")
            lines.append("")

            # Bonus subraza.
            if subr.get("ability_bonuses") != []:
                lines.append(f"Subrace Bonuses:")
                for ab in subr.get("ability_bonuses", []):
                    lines.append(f"  -{ab['ability_score']['name']}: +{ab['bonus']}")
                lines.append("")

            # Rasgos de subraza.
            if subr.get("racial_traits") != []:
                lines.append("Subrace Traits:")
                for t in subr.get("racial_traits", []):
                    lines.append(f"  -{t['name'].upper()}:")
                    subrt:dict = api.get_trait(t['index'])
                    for d in subrt.get("desc", []):
                        lines.append(f"  {d}")
                    lines.append("")

    return "\n".join(lines)



# <---> <---> <---> <---> <---> <--->



def format_spell(data: dict) -> str:
    lines = []

    # TITULO : Nombre del conjuro seguido de un separador estético.
    lines.append(data["name"].upper())
    lines.append("_" * 20)
    lines.append("")

    # CUERPO : Escuela, nivel, componentes, materiales, duración, tiempo de lanzamiento, concentración, ritual y rango.
    lines.append(f"School: {data['school']['name']} - lvl {data.get('level')}")

    l = ""
    if data.get('material') != []:
        l=f"Components: {data.get('components')} - Material: {data.get('material')}"
    else :
        l=f"Components: {data.get('components')}"
    lines.append(l)

    lines.append(f"Duration: {data.get('duration')} - Casting Time: {data.get('casting_time')}")
    lines.append(f"Concentration: {data.get('concentration')} - Ritual: {data.get('ritual')}")
    lines.append(f"Range: {data.get('range')} ")
    lines.append("")

    # DESCRIPCIÓN : Descripción y niveles superiore.
    lines.append(f"Descripción:")
    for d in data.get("desc", []):
        lines.append(f"  {d}")
    for d in data.get("higher_level", []):
        lines.append(f"  {d}")

    return "\n".join(lines)



# <---> <---> <---> <---> <---> <--->



def format_skill(data: dict) -> str:
    lines = []

    # TITULO : Nombre de la habilidad seguido de un separador estético.
    lines.append(data["name"].upper())
    lines.append("_" * 20)
    lines.append("")

    # CUERPO : Estadiística de habilidad.
    ability = data["ability_score"]["name"]
    lines.append(f"Ability: {ability}")
    lines.append("")

    # DESCRIPCIÓN : Descripción.
    lines.append("Description:")
    for d in data.get("desc", []):
        lines.append(f"  {d}")

    return "\n".join(lines)



# <---> <---> <---> <---> <---> <--->



def format_equipment(data: dict) -> str:
    lines = []

    # TITULO : Nombre del equipo seguido de un separador estético.
    lines.append(data["name"].upper())
    lines.append("_" * 20)
    lines.append("")

    # CUERPO : Categorias, coste, peso, propiedades y contenidos.
    if "equipment_category" in data:
        lines.append(f"Eqipment Category: {data['equipment_category']['name']}")

    if "gear_category" in data:
        lines.append(f"Gear Category: {data['gear_category']['name']}")
    lines.append("")

    if "cost" in data:
        lines.append(
            f"Cost: {data['cost']['quantity']} {data['cost']['unit']}"
        )

    if "weight" in data:
        lines.append(f"Weight: {data['weight']} lb")
    lines.append("")

    if data.get("properties") != []:
        lines.append("")
        lines.append("Properties:")
        for d in data["properties"]:
            lines.append(f"  {d}")

    if data.get("contents") != []:
        lines.append("")
        lines.append("Contents:")
        for d in data["contents"]:
            lines.append(f"  {d}")

    # DESCRIPCIÓN : Descripción.
    if data.get("desc") != []:
        lines.append("")
        lines.append("Description:")
        for d in data["desc"]:
            lines.append(f"  {d}")

    return "\n".join(lines)
