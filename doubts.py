# Draw a diagram that represents the user 
# dictionary: 
# user = {'id': 101,
#          'name': 'Alice', ''
#          'roles': ['editor', 'viewer']} in memory. Show how the variables user, id, name,
# and roles point to their respective data objects.
user------------------> {'id': id_obj,'name': name_obj,'roles':roles_list}
id_obj ------->101
name_ibje--------->ALice
roles_list -------->["editor","viewer"]
