#!/usr/bin/env python3

import requests
import unicodedata

# methods

def slugified(value):
  value = str(value)
  value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
  value = value.lower()
  value = value.replace(' ', '-')
  return value


def slug_exists(environment_name, environments):
  return next(
    (
      x for x in environments if (
        x['slug'] == slugified(environment_name)
      )
    ),
    None
  ) is not None


def prompt_for_new_environment_name(environments):
  output_environment = input('Name of new environment: ')

  if slug_exists(output_environment, environments):
    print(f'Environment with slug {output_environment} already exists in {repository}')
    return prompt_for_new_environment_name(environments)

  return output_environment


def prompt_for_action(old_variable):
  action = input('[C]opy existing value, [F]ind and replace, [N]ew: ')

  if action.lower() in ['c', 'copy']:
    new_value = old_variable['value']
  elif action.lower() in ['f', 'find']:
    find = input('Find: ')
    replace = input('Replace with: ')

    new_value = old_variable['value'].replace(find, replace)
  elif action.lower() in ['n', 'new', '']:
    value_input = input(f'New value (leave blank for "TODO"): ')

    if value_input == '':
      new_value = 'TODO'
    else:
      new_value = value_input
  else:
    return prompt_for_action(old_variable)
  
  return new_value
  

def prompt_for_new_variable(old_variable):
  variable_json = {
    'key': old_variable['key'],
    'value': old_variable,
    'secured': old_variable['secured'],
  }
    
  print(f'Update variable: {old_variable["key"]} (current value: {old_variable["value"]}):')
  new_value = prompt_for_action(old_variable)

  return {**variable_json, 'value': new_value}


def clone_environment(environments, input_environment, old_variables, headers, repo_url):
  create_environment_api = f'{repo_url}/environments'
  output_environment = prompt_for_new_environment_name(environments)
  new_environment_type = input('Type of new environment, e.g. test, staging, production: ')
  new_variables = []

  for variable in old_variables:
    if variable['secured']:
      new_variables.append({**variable, 'value': 'TODO'})
    else:
      new_variables.append(prompt_for_new_variable(variable))

  print(f'Creating new environment {output_environment} in {workspace}/{repository}/{new_environment_type}...')

  create_environment_response = requests.post(
    create_environment_api,
    headers = headers,
    json = {
      'name': output_environment,
      'environment_type': {
        'name': new_environment_type
      }
    }
  )

  new_environment_json = create_environment_response.json()
  new_environment_uuid = new_environment_json['uuid'][1:-1]

  if create_environment_response.status_code != 201:
    print(f'Failed to create new environment {output_environment}')
    print(create_environment_response.json())
    try_again = input('Try again? (y/N): ')

    if try_again.lower() in ['y', 'yes']:
      clone_environment(environments, input_environment, old_variables, headers, repo_url)
    else:
      exit()

  print(f'Success! UUID: {new_environment_uuid}')

  updated_variables = []

  for item in new_variables:
    create_variable_api = f'{repo_url}/deployments_config/environments/%7B{new_environment_uuid}%7D/variables'

    create_variable_response = requests.post(
      create_variable_api,
      headers = headers,
      json = item
    )

    if create_variable_response.status_code != 201:
      print(f'Failed to create new variable {item["key"]} :(')
    else:
      updated_variables.append(item)

  print(f'Successfully added {len(updated_variables)} variables:')

  for variable in updated_variables:
    print(f'{variable["key"]} = {variable["value"]}')

  clone_again = input(f'Clone {input_environment} again? (y/N): ')

  if clone_again.lower() in ['y', 'yes']:
    clone_environment(environments, input_environment, old_variables, headers, repo_url)


def clone_from_repo(repo_url, headers):
  environments_api = f'{repo_url}/environments'

  environments_response = requests.get(
    environments_api,
    headers = headers
  )

  environments_response_json = environments_response.json()
  environments = environments_response_json['values']

  print(f'Found {len(environments)} environments in {repository}:')

  for environment in environments:
    print(f'{environment["name"]} ({environment["slug"]}) in {environment["environment_type"]["name"]}')

  input_environment = slugified(input('Name or slug of environment to clone: '))

  selected_environment = next(
    (
      x for x in environments if (
        x['slug'] == input_environment
      )
    ),
    None
  )

  if selected_environment is None:
    print(f"Couldn't find an environment with the slug {input_environment}, in {repository}")
    exit()

  print(f"Found environment {selected_environment['uuid']} in {selected_environment['environment_type']['name']}")

  environment_uuid = selected_environment['uuid'][1:-1]

  variables_api = f'{repo_url}/deployments_config/environments/%7B{environment_uuid}%7D/variables'

  variables_response = requests.get(
    variables_api,
    headers = headers
  )

  variables_response_json = variables_response.json()
  old_variables = variables_response_json['values']
  post_headers = {**headers, 'Content-Type': 'application/json'}

  clone_environment(environments, input_environment, old_variables, post_headers, repo_url)

  clone_again_from_repo = input(f'Clone another environment from {repository}? (y/N): ')

  if clone_again_from_repo.lower() in ['y', 'yes']:
    clone_from_repo(repo_url, headers)

def main():
  while True:
    workspace = input('Bitbucket workspace slug: ')
    repository = input('Bitbucket repository slug: ')
    auth_token = input('Bitbucket repository access token: ')

    repo_url = f'https://api.bitbucket.org/2.0/repositories/{workspace}/{repository}'
    headers = {
      'Authorization': f'Bearer {auth_token}',
      'Accept': 'application/json',
    }

    clone_from_repo(repo_url, headers)

    clone_from_new_repo = input(f'Clone an environment from another repository? (y/N): ')

    if clone_from_new_repo.lower() not in ['y', 'yes']:
      exit()

if __name__ == '__main__':
  main()