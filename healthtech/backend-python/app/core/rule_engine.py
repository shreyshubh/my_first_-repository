RULES = {
    ("CODEINE", "CYP2D6", "Poor Metabolizer"): {
        "risk_label": "Avoid",
        "severity": "high",
        "recommendation": "Avoid codeine due to reduced conversion to active metabolite.",
    },
    ("CLOPIDOGREL", "CYP2C19", "Poor Metabolizer"): {
        "risk_label": "Use Alternative",
        "severity": "high",
        "recommendation": "Consider alternative antiplatelet therapy.",
    },
    ("WARFARIN", "CYP2C9", "Poor Metabolizer"): {
        "risk_label": "Dose Reduce",
        "severity": "moderate",
        "recommendation": "Start with reduced dosing and monitor INR closely.",
    },
    ("SIMVASTATIN", "SLCO1B1", "Decreased Function"): {
        "risk_label": "Myopathy Risk",
        "severity": "moderate",
        "recommendation": "Use lower dose or alternative statin.",
    },
    ("AZATHIOPRINE", "TPMT", "Low Activity"): {
        "risk_label": "Severe Toxicity Risk",
        "severity": "high",
        "recommendation": "Substantially reduce dose or use alternative therapy.",
    },
    ("FLUOROURACIL", "DPYD", "No Function"): {
        "risk_label": "Contraindicated",
        "severity": "high",
        "recommendation": "Avoid fluoropyrimidine therapy.",
    },
}


def evaluate_drug_rules(drugs: list[str], gene_phenotypes: list[dict[str, str]]) -> list[dict[str, str]]:
    recommendations: list[dict[str, str]] = []

    for drug in drugs:
        for entry in gene_phenotypes:
            key = (drug, entry["gene"], entry["phenotype"])
            rule = RULES.get(key)
            if not rule:
                continue

            recommendations.append(
                {
                    "drug": drug,
                    "gene": entry["gene"],
                    "phenotype": entry["phenotype"],
                    "risk_label": rule["risk_label"],
                    "severity": rule["severity"],
                    "recommendation": rule["recommendation"],
                }
            )

    if recommendations:
        return recommendations

    return [
        {
            "drug": drug,
            "gene": "N/A",
            "phenotype": "N/A",
            "risk_label": "No Actionable PGx Rule Found",
            "severity": "low",
            "recommendation": "No deterministic gene-drug rule matched current inputs.",
        }
        for drug in drugs
    ]
