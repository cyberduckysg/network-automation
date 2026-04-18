
# Your NaaS monitoring tool - first building block


spine_switches = [

    "10.0.0.1", # Spine-01
    "10.0.0.2", # Spine-02
]


leaf_switches = [

    "10.1.1.1", # leaf-01
    "10.1.1.2", # leaf-02
    "10.1.1.3", # leaf-03
]

print("====== Spine Layer =====")
for ip in spine_switches:
    print(f" checking spine : {ip}")

print("==== Leaf Layer ====")
for ip in leaf_switches:
    print(f" checking leaf: {ip}")

print(" Scan complete")