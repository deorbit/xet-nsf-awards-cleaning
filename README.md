# Submodule Your Assets

This repository demonstrates using Git submodules to add a [XetHub](https://xethub.com/) repository to another remote. In this case, a repository hosted on GitHub.

This pattern is especially useful when reading from and writing to a XetHub repository (e.g., versioned data or machine learning models) while keeping your code on another version control platform.

The key benefits to this setup:

- Efficiently version data, models, and other large assets on XetHub
- Keep collaboration around your code in another platform
- Simplicity in reading and writing; submoduled repositories and their contents are accessible as a directory within the parent project
- Maintain separate repositories and version history for both projects

Read more about how the connection between the XetHub repository, [`nsf-awards`](https://xethub.com/XetHub/nsf-awards), and this GitHub repository is established and maintained in the [XetHub documentation](https://xethub.com/assets/docs/large-repos/using-submodules#simple-data-cleaning-example).
