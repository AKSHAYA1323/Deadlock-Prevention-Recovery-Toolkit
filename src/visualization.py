import networkx as nx
import matplotlib.pyplot as plt
import io
import base64

def draw_resource_allocation_graph(processes, allocation, available):
    """
    Draws a Resource Allocation Graph (RAG) showing process-resource interactions.
    Returns the graph as a base64 encoded image string.
    """
    G = nx.DiGraph()

    # Create nodes for processes and resources
    process_nodes = [f"P{i+1}" for i in range(len(processes))]
    resource_nodes = [f"R{j+1}" for j in range(len(available))]

    G.add_nodes_from(process_nodes, shape="circle", color="blue")  # Processes
    G.add_nodes_from(resource_nodes, shape="square", color="red")  # Resources

    # Add edges for allocated resources
    for i, process in enumerate(processes):
        for j, res in enumerate(allocation[i]):
            if res > 0:
                G.add_edge(resource_nodes[j], process_nodes[i], label=f"Allocated {res}")

    # Add edges for requested resources (need-claim edges)
    # For this we need to calculate the need matrix (max_demand - allocation)
    # Since we don't have max_demand here, we'll just show allocation edges

    # Draw graph
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)  # For consistent layout

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, 
                          nodelist=process_nodes, 
                          node_color='lightblue',
                          node_size=2000, 
                          node_shape='o')
    
    nx.draw_networkx_nodes(G, pos, 
                          nodelist=resource_nodes, 
                          node_color='lightgreen',
                          node_size=1500, 
                          node_shape='s')
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=2, arrowsize=20)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    # Draw edge labels
    edge_labels = {(u, v): d.get("label", "") for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Resource Allocation Graph (RAG)")
    plt.axis('off')
    
    # Save figure to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    plt.close()
    
    # Encode the image to base64
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode()
    
    return img_str

def get_resource_allocation_graph_html(processes, allocation, available):
    """
    Returns HTML img tag with the resource allocation graph.
    """
    img_str = draw_resource_allocation_graph(processes, allocation, available)
    return f'<img src="data:image/png;base64,{img_str}" alt="Resource Allocation Graph">'
