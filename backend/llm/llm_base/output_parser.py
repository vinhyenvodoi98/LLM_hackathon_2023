import json

class OutputParser:

    @staticmethod
    def json_extract(output):
        json_start_index = output.find("$")
        json_end_index = output.rfind("&")

        json_string = output[json_start_index:json_end_index + 1]
        correct_formatted_json_string = json_string.replace("$", "{").replace("&", "}").replace("\n", "")
        json_object = json.loads(correct_formatted_json_string)
        return json_object
