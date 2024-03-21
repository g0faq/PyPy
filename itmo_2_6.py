import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
graph = nx.Graph()

# Vertices in the code
vertices = ['gcc-12-base', 'dict', 'gdisk', 'gpgv', 'htop', 'libacl1', 'libblkid1', 'libbz2-1.0', 'libc6', 'libc6',
            'libc6', 'libcap2', 'libcrypt1', 'libcrypt1', 'libevent-core-2.1-7', 'libgcc-s1', 'libgcc-s1', 'libgcc-s1',
            'libcrypt20', 'libgpg-error0', 'libmaa4', 'libmount1', 'libncursesw6', 'libnl-3-200', 'libnl-genl-3-200',
            'libpcre2-8-0', 'libpopt0', 'librecode0', 'libselinux1', 'libsmartcols1', 'libstdc++6', 'libinfo6',
            'libutempter0', 'libuuid1', 'mount', 'netbase', 'recode', 'sed', 'tar', 'tmux', 'zlib1g', 'zsh',
            'zsh-common', 'libncursesw6']

  # Replace with your own words
graph.add_nodes_from(vertices)


# Function to connect vertices
def connect_vertices(graph, vertex1, vertex2):
    graph.add_edge(vertex1, vertex2)


# User input for connecting vertices
while True:
    choices = input().split()
    if choices == ['end']:
        break

    connect_vertices(graph, choices[0], choices[1])

# Print the edges of the graph
print("Graph edges:", graph.edges())

# Visualization using matplotlib
pos = nx.spring_layout(graph)  # Positioning of nodes
nx.draw(graph, pos, with_labels=True, font_weight='bold')
plt.show()