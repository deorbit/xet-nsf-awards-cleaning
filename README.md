# Submodule Your Assets

This repository demonstrates using Git submodules to add a [XetHub](https://xethub.com/) repository to another remote. In this case, a repository hosted on GitHub.

This pattern is especially useful when reading from and writing to a XetHub repository (e.g., versioned data or machine learning models) while keeping your code on another version control platform like GitHub.

The key benefits to this setup:

- Efficiently version data, models, and other large assets on XetHub
- Keep collaboration around your code on GitHub
- Simplicity in reading and writing; submoduled repositories and their contents are accessible as a directory within the parent project
- Maintain separate repositories and version history for both projects

Read more about how the connection between the two project is established and maintained in the XetHub documendation.
