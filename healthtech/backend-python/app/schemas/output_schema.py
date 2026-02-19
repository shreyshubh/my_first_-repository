from pydantic import BaseModel


class PatientSummary(BaseModel):
    genes_detected: list[str]
    variants_considered: int
    drugs_requested: list[str]


class MatchedVariant(BaseModel):
    gene: str
    star_allele: str
    rsid: str | None = None
    phenotype: str


class DrugRecommendation(BaseModel):
    drug: str
    gene: str
    phenotype: str
    risk_label: str
    severity: str
    recommendation: str


class ConfidenceBreakdown(BaseModel):
    variant_impact: float
    gene_drug_relevance: float
    guideline_support: float
    data_completeness: float


class Confidence(BaseModel):
    score: float
    breakdown: ConfidenceBreakdown


class AnalyzeResponse(BaseModel):
    patient_summary: PatientSummary
    matched_variants: list[MatchedVariant]
    drug_recommendations: list[DrugRecommendation]
    confidence: Confidence
    explanation: str
    disclaimer: str
