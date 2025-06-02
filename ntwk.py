import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 查重率服从什么分布
# 查重率应该服从什么分布
# 假设和经验：几乎没有作弊，不存在小团体作弊


# 创建一个示例图

t = []
with open('SD_sticks.csv', 'r') as file:
    for line in file:
        province, problem, u, v, weight = line.strip().split(',')
        t.append((weight, u, v))
t = sorted(t)
t = t[ : : -1]
t = [(u, v) for (weight, u, v) in t]

colors = []
G = nx.Graph()
for (u, v) in t:
    G.add_edge(u, v)
    if   len(G.nodes) <= 2265 * 0.1:
        while len(colors) < len(G.nodes):
            colors.append((1, 0, 0))
    elif len(G.nodes) <= 2265 * 0.3:
        while len(colors) < len(G.nodes):
            colors.append((0, 1, 0))
    elif len(G.nodes) <= 2265 * 0.6:
        break
        while len(colors) < len(G.nodes):
            colors.append((0, 0, 1))
pos = nx.spring_layout(G, seed = 42)

# 初始化图形
fig, ax = plt.subplots()

# 绘制节点
nodes = nx.draw_networkx_nodes(G, pos, node_size = 10)

edges = nx.draw_networkx_edges(G, pos)
edge_artists = edges.get_segments()  # 获取边的线段信息
num_edges = len(edge_artists)


aza = 0
# 动画更新函数
def update(frame):
    global aza
    if True or frame == 0 and aza == 0:
        aza += 1
    # 动态调整边的透明度
        alpha_values = [1 if i <= frame else 1 for i in range(num_edges)]
        edges.set_alpha(alpha_values)

        global G
        global colors
        s = 0
        print('@')
        for t in G.nodes:
            if t in ['SD-J02255','SD-J02249']:
                colors[s] = (0.3, 0.5, 0.7)
                print(s, t)
            s += 1
        print('$')
        nodes.set_facecolor(colors)
    return [edges, nodes]

# 创建动画
ani = FuncAnimation(fig, update, frames=num_edges, interval=100, repeat = False, blit=True)

# 显示动画
plt.show()

# 保存为 GIF（可选）
# ani.save("graph_edges_animation.gif", writer="imagemagick")
