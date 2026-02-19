from pydantic import BaseModel, ConfigDict


class StrictBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PatientSummary(StrictBaseModel):
    genes_detected: list[str]
    variants_considered: int
    drugs_requested: list[str]


class MatchedVariant(StrictBaseModel):
    gene: str
    star_allele: str
    rsid: str | None = None
    phenotype: str


class DrugRecommendation(StrictBaseModel):
    drug: str
    gene: str
    phenotype: str
    risk_label: str
    severity: str
    recommendation: str


class ConfidenceBreakdown(StrictBaseModel):
    variant_impact: float
    gene_drug_relevance: float
    guideline_support: float
    data_completeness: float


class Confidence(StrictBaseModel):
    score: float
    breakdown: ConfidenceBreakdown


class AnalyzeResponse(StrictBaseModel):
    patient_summary: PatientSummary
    matched_variants: list[MatchedVariant]
    drug_recommendations: list[DrugRecommendation]
    confidence: Confidence
    explanation: str
    disclaimer: str
