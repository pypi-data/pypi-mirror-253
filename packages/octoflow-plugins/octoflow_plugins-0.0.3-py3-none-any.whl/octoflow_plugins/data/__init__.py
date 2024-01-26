from octoflow.plugin import Package

__all__ = [
    "package",
]

package = Package(
    "loaders",
    modules=[
        {
            "name": ".loaders",
            "package": "octoflow_plugins.data",
        },
    ],
)
