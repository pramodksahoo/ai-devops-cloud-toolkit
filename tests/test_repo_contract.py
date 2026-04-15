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
        rendered = subprocess.run(
            ['kubectl', 'kustomize', str(ROOT / 'platform/kubernetes/overlays/local-kind')],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertIn('kind: Deployment', rendered.stdout)
        self.assertIn('name: demo-app', rendered.stdout)
        self.assertIn('kind: ConfigMap', rendered.stdout)

    def test_yaml_files_parse(self):
        subprocess.run(
            [
                'ruby',
                '-e',
                "require 'yaml'; Dir['.github/workflows/*.yml', 'platform/kubernetes/**/*.yaml', 'platform/workloads/**/*.yaml', '.config/**/*.yml', '.config/**/*.yaml'].sort.each { |f| YAML.load_file(f) }",
            ],
            check=True,
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_workload_boundary_contract(self):
        base_kustomization = (ROOT / 'platform/kubernetes/base/kustomization.yaml').read_text()
        workload_kustomization = (ROOT / 'platform/workloads/demo-app/manifests/kustomization.yaml').read_text()
        workload_deployment = (ROOT / 'platform/workloads/demo-app/manifests/deployment.yaml').read_text()
        workload_service = (ROOT / 'platform/workloads/demo-app/manifests/service.yaml').read_text()
        workload_content = (ROOT / 'platform/workloads/demo-app/manifests/index.html').read_text()

        self.assertIn('../../workloads/demo-app/manifests', base_kustomization)
        self.assertIn('deployment.yaml', workload_kustomization)
        self.assertIn('service.yaml', workload_kustomization)
        self.assertIn('configMapGenerator', workload_kustomization)
        self.assertIn('index.html', workload_kustomization)
        self.assertIn('name: demo-app', workload_deployment)
        self.assertIn('name: demo-app', workload_service)
        self.assertIn('AI DevOps Cloud Toolkit', workload_content)

        for rel in (
            'platform/kubernetes/base/deployment.yaml',
            'platform/kubernetes/base/service.yaml',
            'platform/kubernetes/base/configmap.yaml',
        ):
            self.assertFalse((ROOT / rel).exists(), rel)

    def test_repo_check_passes(self):
        subprocess.run(
            ['python3', str(ROOT / 'scripts/repo_check.py')],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_provider_sample_contract(self):
        provider_sample = (ROOT / 'examples/provider-sample/README.md').read_text()
        provider_template = (ROOT / 'examples/provider-sample/providers/TEMPLATE.md').read_text()
        provider_modules = (ROOT / 'examples/provider-sample/modules/README.md').read_text()
        provider_manifests = (ROOT / 'examples/provider-sample/manifests/README.md').read_text()
        provider_notes = (ROOT / 'examples/provider-sample/docs/extension-notes.md').read_text()
        provider_guide = (ROOT / 'docs/examples/provider-sample.md').read_text()
        examples_index = (ROOT / 'examples/README.md').read_text()
        docs_examples_index = (ROOT / 'docs/examples/README.md').read_text()

        self.assertIn('example-only', provider_sample.lower())
        self.assertIn('officially supports a cloud provider', provider_sample)
        self.assertIn('providers/', provider_sample)
        self.assertIn('modules/', provider_sample)
        self.assertIn('manifests/', provider_sample)
        self.assertIn('docs/', provider_sample)

        self.assertIn('future provider-oriented example', provider_template)
        self.assertIn('example-only', provider_modules.lower())
        self.assertIn('example-only', provider_manifests.lower())
        self.assertIn('prompts/add-example.md', provider_notes)

        self.assertIn('example-only', provider_guide.lower())
        self.assertIn('prompts/add-example.md', provider_guide)
        self.assertIn('canonical local-first path', provider_guide)
        self.assertIn('platform/', provider_guide)

        self.assertIn('provider-sample/', examples_index)
        self.assertIn('provider-sample.md', docs_examples_index)


if __name__ == '__main__':
    unittest.main()
