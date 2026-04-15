import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepoContractTests(unittest.TestCase):
    def test_scripts_are_present(self):
        for rel in [
            'scripts/bootstrap.sh',
            'scripts/validate.sh',
            'scripts/demo-up.sh',
            'scripts/demo-verify.sh',
            'scripts/demo-down.sh',
            'scripts/install-validation-tools.sh',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_kustomize_overlay_renders(self):
        subprocess.run(
            ['kubectl', 'kustomize', str(ROOT / 'platform/kubernetes/overlays/local-kind')],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_yaml_files_parse(self):
        subprocess.run(
            [
                'ruby',
                '-e',
                "require 'yaml'; Dir['.github/workflows/*.yml', 'platform/kubernetes/**/*.yaml', '.config/**/*.yml', '.config/**/*.yaml'].sort.each { |f| YAML.load_file(f) }",
            ],
            check=True,
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_repo_check_passes(self):
        subprocess.run(
            ['python3', str(ROOT / 'scripts/repo_check.py')],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


if __name__ == '__main__':
    unittest.main()
