from octoflow.plugin import Package

__all__ = [
    "package",
]

package = Package(
    "artifacts",
    modules=[
        {
            "name": ".json_",
            "package": "octoflow_plugins.tracking.artifacts",
        },
        {
            "name": ".pandas_",
            "package": "octoflow_plugins.tracking.artifacts",
        },
        {
            "name": ".pickle_",
            "package": "octoflow_plugins.tracking.artifacts",
        },
        {
            "name": ".transformers_",
            "package": "octoflow_plugins.tracking.artifacts",
        },
    ],
)
