# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['no_action']

package_data = \
{'': ['*'], 'no_action': ['templates/*']}

install_requires = \
['jinja2>=3.1.3,<4.0.0']

setup_kwargs = {
    'name': 'no-action',
    'version': '0.4.0',
    'description': 'no_action is an incremental automation library to eliminate toil in processes.',
    'long_description': "# no_action\n\n## Integrate with your tools\n\n- [ ] [Set up project integrations](https://gitlab.com/Skoretz/no_action/-/settings/integrations)\n\n## Test and Deploy\n\nUse the built-in continuous integration in GitLab.\n\n- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)\n- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing\n  (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)\n- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto\n  Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)\n- [ ] [Use pull-based deployments for improved Kubernetes\n  management](https://docs.gitlab.com/ee/user/clusters/agent/)\n- [ ] [Set up protected\n  environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)\n\n## Editing this README\n\nWhen you're ready to make this README your own, just edit this file and use the handy template below\n(or feel free to structure it however you want - this is just a starting point!). Thanks to\n[makeareadme.com](https://www.makeareadme.com/) for this template.\n\n## Suggestions for a good README\n\nEvery project is different, so consider which of these sections apply to yours. The sections used in\nthe template are suggestions for most open source projects. Also keep in mind that while a README\ncan be too long and detailed, too long is better than too short. If you think your README is too\nlong, consider utilizing another form of documentation rather than cutting out information.\n\n## Name\n\nChoose a self-explaining name for your project.\n\n## Description\n\nLet people know what your project can do specifically. Provide context and add a link to any\nreference visitors might be unfamiliar with. A list of Features or a Background subsection can also\nbe added here. If there are alternatives to your project, this is a good place to list\ndifferentiating factors.\n\n## Badges\n\nOn some READMEs, you may see small images that convey metadata, such as whether or not all the tests\nare passing for the project. You can use Shields to add some to your README. Many services also have\ninstructions for adding a badge.\n\n## Visuals\n\nDepending on what you are making, it can be a good idea to include screenshots or even a video\n(you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out\nAsciinema for a more sophisticated method.\n\n## Installation\n\nWithin a particular ecosystem, there may be a common way of installing things, such as using Yarn,\nNuGet, or Homebrew. However, consider the possibility that whoever is reading your README is\na novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people\nto using your project as quickly as possible. If it only runs in a specific context like\na particular programming language version or operating system or has dependencies that have to be\ninstalled manually, also add a Requirements subsection.\n\n## Usage\n\nUse examples liberally, and show the expected output if you can. It's helpful to have inline the\nsmallest example of usage that you can demonstrate, while providing links to more sophisticated\nexamples if they are too long to reasonably include in the README.\n\n## Support\n\nTell people where they can go to for help. It can be any combination of an issue tracker, a chat\nroom, an email address, etc.\n\n## Roadmap\n\nIf you have ideas for releases in the future, it is a good idea to list them in the README.\n\n## Contributing\n\nState if you are open to contributions and what your requirements are for accepting them.\n\nFor people who want to make changes to your project, it's helpful to have some documentation on how\nto get started. Perhaps there is a script that they should run or some environment variables that\nthey need to set. Make these steps explicit. These instructions could also be useful to your future\nself.\n\nYou can also document commands to lint the code or run tests. These steps help to ensure high code\nquality and reduce the likelihood that the changes inadvertently break something. Having\ninstructions for running tests is especially helpful if it requires external setup, such as starting\na Selenium server for testing in a browser.\n\n## Authors and acknowledgment\n\nShow your appreciation to those who have contributed to the project.\n\n## License\n\nFor open source projects, say how it is licensed.\n\n## Project status\n\nIf you have run out of energy or time for your project, put a note at the top of the README saying\nthat development has slowed down or stopped completely. Someone may choose to fork your project or\nvolunteer to step in as a maintainer or owner, allowing your project to keep going. You can also\nmake an explicit request for maintainers.\n",
    'author': 'Nicholas Skoretz',
    'author_email': 'nskoretz@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
