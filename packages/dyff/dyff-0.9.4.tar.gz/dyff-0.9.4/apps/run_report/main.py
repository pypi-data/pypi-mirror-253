# Copyright UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

# mypy: disable-error-code="import-untyped"
import absl.app
import absl.flags
import ruamel.yaml
from absl import logging
from ruamel.yaml.compat import StringIO as YAMLStringIO

from dyff.api import storage
from dyff.audit.scoring import Rubric
from dyff.core import dynamic_import
from dyff.schema.dataset import arrow

# -----------------------------------------------------------------------------

FLAGS = absl.flags.FLAGS

absl.flags.DEFINE_string(
    "report_yaml", None, "Path to a YAML file containing the Report manifest."
)
absl.flags.mark_flag_as_required("report_yaml")

# -----------------------------------------------------------------------------


def main(_unused_argv) -> None:
    logging.set_verbosity(logging.INFO)

    yaml = ruamel.yaml.YAML()
    with open(FLAGS.report_yaml, "r") as fin:
        report_yaml = yaml.load(fin)
    yaml_string = YAMLStringIO()
    yaml.dump(report_yaml, yaml_string)
    logging.info(f"report_yaml:\n{yaml_string.getvalue()}")

    report_id = report_yaml["spec"]["id"]

    evaluation_id = report_yaml["spec"]["evaluation"]
    dataset_id = report_yaml["spec"]["dataset"]

    report_type = report_yaml["spec"]["report"]
    rubric: Rubric = dynamic_import.instantiate(f"dyff.audit.scoring.{report_type}")

    task_data = arrow.open_dataset(storage.paths.dataset_root(dataset_id))
    outputs_data = arrow.open_dataset(storage.paths.outputs_verified(evaluation_id))

    # TODO: We're not doing anything with the DataViews yet

    arrow.write_dataset(
        rubric.apply(task_data, outputs_data),
        output_path=storage.paths.report_root(report_id),
        feature_schema=rubric.schema,
    )


if __name__ == "__main__":
    absl.app.run(main)
