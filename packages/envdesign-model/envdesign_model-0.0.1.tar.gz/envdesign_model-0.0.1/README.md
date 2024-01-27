# AzQualify-EnvDesign-Model

A domain-agnostic model for determining optimal hardware/software testing configurations using graph theory and optimization algorithms. The model is packaged into a Python module that is imported and used in the larger AzQualify EnvDesign system. 

## Getting Started

1. Install conda from the conda website, [https://conda.io/projects/conda/en/latest/user-guide/install/index.html]
(https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
1. Create a Python3 virtual environment using conda with the command `conda create -n <envname> python=3.9.17`
2. Activate the virtual environment with the command: `conda activate <envname>`
3. Clone the code from [https://msazure.visualstudio.com/One/_git/AzQualify-EnvDesign-Model](https://msazure.visualstudio.com/One/_git/AzQualify-EnvDesign-Model)
4. Install the dependencies with the command `pip install -r requirements.txt`
5. Install the library in the virtual environment with the command `python setup.py install`
7. To run unit tests, run the command `pytest`
8. To deactivate the virtual environment, run the command `conda deactivate`

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
