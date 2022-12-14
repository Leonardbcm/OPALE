from src.models.GNNWrapper import GNNWrapper

def ch(c1, c2, h=None):
    if h is None: return f"from_{c1}_to_{c2}"
    return f"from_{c1}_to_{c2}_{h}"

def map_fname(n):
    if "ATC" not in n:
        z = n.split("_")[0]
        f = n.split("_")[1]
        return f"{z}_{f}"
    else:
        z = n.split("_")[2]
        zprime = n.split("_")[4]
        return f"{z}_{zprime}" 

def map_middle_version(v):
    if v == "atc": return "\\textbf{A}"
    if v == "flux": return "\\textbf{F}"    
    if v == "lin_prog": return "\\textbf{Flin}"
    if v == "least_square": return "\\textbf{Flsq}"
    if v == "combined": return "\\textbf{Fcmb}"
    if v == "combined_unilateral": return "\\textbf{Fos}"

def map_model_name(m):
    if "CNN" in m: return "CNN"
    if "GNN" in m: return "GNN"
    if "DNN" in m: return "DNN"
    return m

def map_new_versions(v):
    model_wrapper = NodeGNNWrapper("FLOWS", "", replace_ATC=v)
    return model_wrapper.replace_ATC_string()

def map_Flux_versions(v):
    nv = map_new_versions(v)
    if nv is None: return ""
    nvs = nv.split("\_")[1]
    if (nvs != "atc") or (nvs != "A"):                          
        nvs = "F" + nvs
    else:
        nvs = "A"
    return nvs
