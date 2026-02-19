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

PHENOTYPE_PRIORITY = {
    "Poor Metabolizer": 5,
    "No Function": 5,
    "Low Activity": 4,
    "Intermediate Metabolizer": 3,
    "Decreased Function": 3,
    "Normal Metabolizer": 2,
    "Normal Activity": 2,
    "Normal Function": 2,
    "Rapid Metabolizer": 1,
    "Indeterminate": 0,
}


def infer_phenotype(gene: str, star_allele: str) -> str:
    allele_tokens = [token.strip().upper() for token in star_allele.replace("|", "/").split("/") if token.strip()]
    if not allele_tokens:
        return "Indeterminate"

    phenotypes = [STAR_PHENOTYPE_MAP.get(gene, {}).get(token, "Indeterminate") for token in allele_tokens]
    return max(phenotypes, key=lambda item: PHENOTYPE_PRIORITY.get(item, 0))
