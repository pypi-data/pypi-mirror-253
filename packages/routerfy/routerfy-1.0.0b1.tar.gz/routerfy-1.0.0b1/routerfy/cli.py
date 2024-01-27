import click
import os
import yaml

from routerfy.utils.config import get_config, get_routes_path
from routerfy.models.aws import AWSServerlessRestApiTemplate, AWSServerlessFunctionTemplate

from distutils.dir_util import copy_tree

module_path = os.path.dirname(os.path.realpath(__file__))

def click_echo_box(text: str):
    middle_part = ("═"*len(text))
    
    click.echo("")
    click.echo("╔"+middle_part+"╗")
    click.echo("║"+text+"║", color=True)
    click.echo("╚"+middle_part+"╝")

@click.group()
def cli():
    pass

@cli.command()
@click.argument('projectname', type=str)
def create(projectname: str):
    click.echo("Checking folder...")
    project_path = os.path.join(os.getcwd(), projectname)
    
    assert not os.path.exists(project_path), f"/{projectname} already exists! Project not created."
    
    os.mkdir(project_path)
    click.echo("Creating configuration file...")
    with open(os.path.join(project_path, "routerfy.config.yaml"), "w") as f:
        yaml.dump({
            "AppName": projectname,
            "Api": {
                "StageName": "default",
                "BuildModel": True
            }
        }, f)
    
    
    click.echo("Copying default routes...")
    
    routes_path = os.path.join(project_path, "routes")
    os.mkdir(routes_path)
    copy_tree(os.path.join(module_path, 'examples', 'routes'), routes_path)
    
    done_message = " Done! Your project was created successfully! "
    
    click_echo_box(done_message)

@cli.command()
def dev():
    from routerfy.development.fastapi import start_api
    start_api()
    
@cli.command()
@click.option('-n', '--version', type=str, help='Select template yaml version type. ["serverless", "resourcefull"]', default='serverless')
def build(version: str):
    click.echo("Preparing environment...")
    config = get_config()
    
    click.echo("Checking routes path...")
    routes_path = get_routes_path(config)
    
    click.echo("Building lambdas template...")
    with click.progressbar(os.listdir(routes_path)) as folders:
        for folder in folders:
            if version == "serverless":
                lambda_template = AWSServerlessFunctionTemplate(src=os.path.join(routes_path, folder), config=config)
            
            lambda_template.build()
            lambda_template.create_template()
            
    click.echo("Building API Gateway template...")
    if version == "serverless":
        api_template = AWSServerlessRestApiTemplate(routes_path=routes_path, config=config)
    
    api_template.build()
    api_template.create_template()
    
    click_echo_box(" Done! Your project was built successfully! ")
        


# @click.option('-n', '--template', type=str, help='Choose if will be "single" or "multiple" templates.', default='multiple')