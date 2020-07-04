import os


def create_expression(input, sequence, func):

    graph = open("../resources/desmos_graph_base.html")
    graph = graph.read()

    expr = func(input)

    # Add another placeholder comment below the expression to allow for further expressions
    graph = graph.replace("<!-- PLACEHOLDER -->", f"{expr} \n <!-- PLACEHOLDER -->")

    sequence.graph = graph

    dir = "../graphs/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    out_graph = open(f"{dir}{sequence.id}.html", "w")
    out_graph.write(graph)


def create_desmos_list(integers):

    desmos_list = str(integers)
    desmos_list = desmos_list.replace("'", "")

    expr = f"calculator.setExpression({{ id: 'graph1', latex:\"{desmos_list}\" }});"
    return expr