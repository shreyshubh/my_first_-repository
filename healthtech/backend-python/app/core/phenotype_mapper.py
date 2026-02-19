STAR_PHENOTYPE_MAP = {
    "CYP2D6": {
        "*3": "Poor Metabolizer",
        "*4": "Poor Metabolizer",
        "*5": "Poor Metabolizer",
        "*10": "Intermediate Metabolizer",
        "*17": "Intermediate Metabolizer",
        "*1": "Normal Metabolizer",
        "*2": "Normal Metabolizer",
    },
    "CYP2C19": {
        "*2": "Poor Metabolizer",
        "*3": "Poor Metabolizer",
        "*17": "Rapid Metabolizer",
        "*1": "Normal Metabolizer",
    },
    "CYP2C9": {
        "*2": "Intermediate Metabolizer",
        "*3": "Poor Metabolizer",
        "*1": "Normal Metabolizer",
    },
    "SLCO1B1": {
        "*5": "Decreased Function",
        "*15": "Decreased Function",
        "*1": "Normal Function",
    },
    "TPMT": {
        "*2": "Low Activity",
        "*3A": "Low Activity",
        "*3C": "Low Activity",
        "*1": "Normal Activity",
    },
    "DPYD": {
        "*2A": "No Function",
        "*13": "No Function",
        "HAPB3": "Decreased Function",
        "*1": "Normal Function",
    },
}


def infer_phenotype(gene: str, star_allele: str) -> str:
    return STAR_PHENOTYPE_MAP.get(gene, {}).get(star_allele.upper(), "Indeterminate")
