import os
import pickle
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import numpy as np
import post_processing

current_output = ''

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.static_folder = 'static'
    app.debug = True
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/get_output')
    def get_output():
        global current_output
        print(current_output)
        return jsonify(text=current_output)

    @app.route('/', methods=['GET', 'POST'])
    def main():
        cleaned_prediction = ""
        global current_output
        analysis_results = {
            "cycle": False,
            "multiple_edges": False,
            "parallel_paths": False
        }
        if request.method == "POST":
            current_output = ''
            openai_api_key = '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'
            client = OpenAI(api_key=openai_api_key)

            input_text = request.form.get("text")
            workflow_to_be_converted = input_text

            query = "Create a mermaid TD graph that describes provided workflow. Do not label edges (except for the if block), all necessary information should be included in nodes. Please include the code only. Use proper block shapes. Name nodes as letters. Make it contain conditional"

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": query + workflow_to_be_converted + "\n"}
                ]
            )

            prediction = completion.choices[0].message.content
            cleaned_prediction = prediction.replace("```", "").replace("mermaid", "")
            current_output = cleaned_prediction
            print(cleaned_prediction)

        if cleaned_prediction:
            graph_edges = post_processing.parse_mermaid_edges(cleaned_prediction)
            post_processing.print_all_edges(graph_edges)
            analysis_results["cycle"] = post_processing.has_cycle_directed(graph_edges)
            analysis_results["multiple_edges"] = post_processing.has_vertex_with_multiple_edges(graph_edges)
            # graph = post_processing.build_graph(graph_edges)
            # analysis_results["parallel_paths"] = post_processing.has_two_different_paths(graph)
            return render_template("website.html", output=cleaned_prediction, analysis_results=analysis_results)
        return render_template("no_input.html")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
