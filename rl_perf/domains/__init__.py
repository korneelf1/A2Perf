import os

cur_path = os.path.dirname(__file__)

# open the file under rl_perf/domains/web_nav/configs/web_navigation_env_config.gin and change the line which specifies: environment.WebNavigationEnv.base_url to the path of the file itself
path = cur_path + '/web_nav/configs/web_navigation_env_config.gin'

target_path = cur_path + '/web_nav/gwob/'
with open(path, 'r') as file:
    data = file.readlines()
    # original_data = file.read()
    # print(original_data)
    
    for i, line in enumerate(data):
        ls = line.split('=')[0].strip()
        if ls == 'environment.WebNavigationEnv.base_url':
            # change this line to current path in the file
            data[i] = "environment.WebNavigationEnv.base_url='file://" + target_path + "'\n"
            # original_data.replace(line, 'environment.WebNavigationEnv.base_url = ' + target_path + '\n')
            

with open(path, 'w') as file:
    for line in data:
        file.write(line)
#     file.write(original_data)
print('done')