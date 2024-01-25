# kedro-expectations
A tool to better integrate Kedro and Great Expectations

## Introduction

Kedro Expectations is a tool designed to make the use of Great Expectations (GX, a data validation tool) within Kedro data science pipelines easier. It is composed of a couple of commands and a hook, allowing the user to create expectation suites and run validations on the Kedro DataCatalog on-the-fly.

## Features

- ⏳ Initialization of GX without having to worry about [datasources](https://docs.greatexpectations.io/docs/terms/datasource)
- 🎯 Creation of [GX suites](https://docs.greatexpectations.io/docs/terms/expectation_suite/) automatically, using the [Data Assistant](https://docs.greatexpectations.io/docs/terms/data_assistant/) profiler
- 🚀 Running validations within the Kedro pipeline on-the-fly

## Installation

You can install the plugin via PyPI:

```bash
pip install kedro-expectations
```


## Usage

### CLI Usage

The first step to use the plugin is running an init command. This command will create the base GX folder and create the only datasource the plugin needs

```bash
kedro expectations init
```

After the init command the plugin is ready to create expectation suites automatically using a DataAssistant profiler. It is possible to create expectation suites for Non-spark dataframe objects (there is no need to worry about the file type since Kedro Expectations used the information from the Kedro data catalog) and Partitioned datasets

Within partitioned datasets, it is possible to create generic expectations, meaning all the partitions will use that expectation, or specific expectations, meaning only the specified partition will use the generated expectation.

Run the following command to create an expectation suite for a given Kedro data set automatically:

```bash
kedro expectations create-suite
```

### Hook Usage

In order to enable the hook capabilities you only need to call it in the settings.py file inside your kedro project

(inside src/your_project_name/settings.py)
```python
from kedro_expectations import KedroExpectationsHooks

HOOKS = (KedroExpectationsHooks(
            on_failure="raise_fast",
            ),
        )
```

### Fail Fast

`on_failure` is a parameter added to give more control over the pipeline. That way it is possible to define, if an expectations validation failure breaks the pipeline run immediately (`on_failure="raise_fast"`), at the end (`on_failure="raise_later`) or not at all(`on_failure="continue"`). Its default value is "continue".

### Notification

With the `notify_config` argument you can set up automatic notifications about the validation run. It uses the GX checkpoint actions to render and send the notification. Currently only notification via email is supported. To set it up, add the following argument to the `KedroExpectationsHooks` object within `settings.py` and modify the addresses and credentials according to your SMTP server and needs.

```python
from kedro_expectations import KedroExpectationsHooks
from kedro_expectations.notification import EmailNotifier

HOOKS = (KedroExpectationsHooks(
            notify_config=EmailNotifier(
              recipients=["john_doe@nobody.io", ],
              sender_login="login",
              sender_password="password",
              smtp_address="smtp.address",
              smtp_port="465"
              )
            ),
        )
```


## Example

To make things clearer, the following example will approach the most complex usage of the plugin, which is when we want to create an specific expectation for a partitioned dataset. It was done using the [Partitioned Iris Starter](https://github.com/ProjetaAi/projetaai-starters/tree/main/for_projetaai/project/partitioned_projetaai)

To start using the plugin, make sure you are in your project's root folder and your pipeline is executing correctly.

Considering you have the plugin installed and the conditions right above are true, the main steps are:
- Run the init command
- Create one or more suites depending on your needs
- Make sure to enable the KedroExpectationsHooks in your project's settings
- Execute the Kedro Pipeline normally 

### Init and Suite Creation

The first step to use the plugin is to use the "kedro expectations init" command. Below we can see the expected result:

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/1_init.png">
</p>

As soon as it is created, we can run the second command: "kedro expectations create-suite"
You will be prompted to choose between (1) suites for generic datasets and (2) suites for partitioned datasets:

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/3_createsuite.png">
</p>

Then we can choose between a generic or specific expectation. In this example, we will press (2) to create a specific one:

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/4_createsuite.png">
</p>

Now the plugin will ask three questions. The first two must be answered based on your project, and the last one is any name based on your preference

Our partitioned dataset structure inside the project:

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/8_createsuite.png">
</p>

Questions asked by the CLI:

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/5_createsuite.png">
</p>

The last step is to decide if we want to exclude some columns from the expectation suite. Whenever you selected your desired columns, type `0`:

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/6_createsuite.png">
</p>

Then your dataset will be validated automatically and will be found at great_expectations/expectations/"your_dataset_name"/"your_expectation_name"

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/7_createsuite.png">
</p>

### Adding the Hook

Now, to be able to test, we only need to add a few lines of code in our settings.py file as shown [above](README.md#hook-usage)

For more information about the functionality of Kedro Hooks, please refer to the [Kedro Hook Documentation](https://kedro.readthedocs.io/en/stable/hooks/introduction.html)

### Running the Kedro project

After adding the Hook there is no extra step. You can simply run the project by typing the default "kedro run" command. 
Whenever a dataset with an existing expectation suite is called by the pipeline, Kedro Expectations will validate it, add the results to the data_docs and (optionally) notify you.

<p align="center">
  <img src="https://gitlab.com/anacision/kedro-expectations/raw/main/images/10_run.png">
</p>

## Contribution

Based on work from Joao Gabriel Pampanin de Abreu. Extended and updated by anacision GmbH since 2023.
Main Developer:
- Marcel Beining (marcel.beining@anacision.de)