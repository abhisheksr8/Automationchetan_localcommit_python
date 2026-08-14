from setuptools import setup, find_packages
setup(
    name = 'Automationchetan_localcommit_python_Pipeline',
    version = '1.0',
    packages = (
      find_packages(include = ('automationchetan_localcommit_python_pipeline*', ))
      + ['prophecy_config_instances', 'prophecy_config_instances.automationchetan_localcommit_python_pipeline']
    ),
    package_dir = {'prophecy_config_instances' : 'configs/resources'},
    package_data = {'prophecy_config_instances.automationchetan_localcommit_python_pipeline' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.17'],
    entry_points = {
'console_scripts' : [
'main = automationchetan_localcommit_python_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
