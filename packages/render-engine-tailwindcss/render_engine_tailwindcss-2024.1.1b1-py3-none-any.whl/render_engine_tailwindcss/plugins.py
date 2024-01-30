from render_engine.plugins import hook_impl
from render_engine.site import Site
from jinja2 import Environment, DictLoader
import logging
import pytailwindcss
import pathlib

default_settings = {
    "static_path": "static",
    "output_path": "output",
    "tailwindcss_cli_input_file": ["tailwind.css"],
    "tailwindcss_config_file": "tailwind.config.js",
}

def build_tailwindcss_config_file(plugins: list[str]|None = None) -> str:
    """Builds the tailwind.config.js file from the plugins list."""
    env = Environment(
        loader=DictLoader(
            {
                "tailwind.config.js": """/** @type {import('tailwindcss').Config}*/
module.exports = {
    content: ['output/**/*.{html, js}']{% if plugins %},
    plugins: [{{","|join(plugins)}}]
    {% else %}
    // plugins: []
{% endif %}}""",
            }
        )
    )
    return env.get_template("tailwind.config.js").render(plugins=plugins) 

def parse_css_files(
        static_path: str | pathlib.Path,
        output_path: str | pathlib.Path,
        ) -> None:

    """
    Parses CSS files in static_path and creates a file for each in output_path
    
    Args:
        static_path: The path to the static folder
        output_path: The path to the output folder
    """

    for input_file in pathlib.Path(static_path).rglob("**/*.css"):
        logging.info(f"Running Tailwind on {input_file=}")
        

        output_file = pathlib.Path(output_path) / pathlib.Path(static_path).name / input_file.relative_to(static_path)
        logging.info(f"{output_file=}")

        pytailwindcss.run(
            auto_install=True,
            tailwindcss_cli_args=[
                "-i",
                f"{input_file.absolute()}",
                "--output",
                output_file,
            ],
        )

class TailwindCSS:
    """A plugin that runs TailwindCSS on the static files."""
    default_settings = default_settings

    @hook_impl
    def pre_build_site(site: "Site") -> None:
        tailwind_config_file = site.plugin_manager.plugin_settings['TailwindCSS']['tailwindcss_config_file']
        if not (config_path:=pathlib.Path(tailwind_config_file)).exists():
            config_path.write_text(
                build_tailwindcss_config_file(
                    plugins=site.plugin_manager.plugin_settings['TailwindCSS'].get('plugins', None)
                )
            )
            
            
    @hook_impl
    def post_build_site(site: "Site") -> None:
        logging.debug("running_post_build_site")
        
        for static_path in site.static_paths:
            parse_css_files(static_path, site.output_path)
