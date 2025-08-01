import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger()


def convert_txt_to_xlsx(input_path: Path, output_dir: Path) -> str:
    """Converts txt to xlsx."""
    logger.debug("[convert_txt_to_xlsx] start converting...")

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    sections = content.split("\n\n")
    airfoil_name = (
        sections[0].split(":")[1].strip().replace("/", "_").replace(" ", "_")
    )

    logger.debug("[convert_txt_to_xlsx] airfoil name: %s", airfoil_name)

    output_path = output_dir / f"{airfoil_name}.xlsx"

    logger.debug("[convert_txt_to_xlsx] output path: %s", output_path)

    upper_data = sections[1].splitlines()[1:]
    lower_data = sections[2].splitlines()[1:]

    upper_df = pd.DataFrame(
        [list(map(float, line.split())) for line in upper_data],
        columns=["Upper X", "Upper Y"],
    )
    lower_df = pd.DataFrame(
        [list(map(float, line.split())) for line in lower_data],
        columns=["Upper X", "Lower Y"],
    )

    logger.debug("[convert_txt_to_xlsx] data shape: %s", upper_df.shape)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        upper_df.to_excel(writer, index=False, sheet_name="Upper Surface")
        lower_df.to_excel(writer, index=False, sheet_name="Lower Surface")

    logger.debug("[convert_txt_to_xlsx] finish converting...")
    return airfoil_name
