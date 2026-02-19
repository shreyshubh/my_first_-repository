ALLOWED_GENES = {"CYP2D6", "CYP2C19", "CYP2C9", "SLCO1B1", "TPMT", "DPYD"}


def parse_info_field(info_field: str) -> dict[str, str]:
    info_map: dict[str, str] = {}
    for item in info_field.split(";"):
        if "=" in item:
            key, value = item.split("=", 1)
            info_map[key.strip().upper()] = value.strip()
    return info_map


def parse_vcf_text(vcf_text: str) -> list[dict[str, str | None]]:
    variants: list[dict[str, str | None]] = []

    for raw_line in vcf_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split("\t")
        if len(parts) < 8:
            continue

        info_map = parse_info_field(parts[7])
        gene = info_map.get("GENE", "").upper()
        if gene not in ALLOWED_GENES:
            continue

        star = info_map.get("STAR")
        rs = info_map.get("RS") or (parts[2] if parts[2] != "." else None)
        if not star:
            continue

        variants.append({"gene": gene, "star": star.upper(), "rs": rs})

    return variants
