from setuptools import setup

with open('README.md', 'r') as oF:
	long_description=oF.read()

setup(
	name='email-smtp',
	version='1.0.0',
	description='',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/ouroboroscoding/email-smtp-python',
	project_urls={
		'Source': 'https://github.com/ouroboroscoding/email-smtp-python',
		'Tracker': 'https://github.com/ouroboroscoding/email-smtp-python/issues'
	},
	keywords=['json'],
	author='Chris Nasr - Ouroboros Coding Inc.',
	author_email='chris@ouroboroscoding.com',
	license='MIT',
	packages=['em'],
	python_requires='>=3.10',
	install_requires=[
		'config-oc>=1.0.3,<1.1',
		'tools-oc>=1.2.3,<1.3',
		'undefined-oc>=1.0.0,<1.1'
	],
	zip_safe=True
)