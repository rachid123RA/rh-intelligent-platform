from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(cv_text, job_description):
    cv_embed = model.encode(cv_text, convert_to_tensor=True)
    jd_embed = model.encode(job_description, convert_to_tensor=True)
    return float(util.cos_sim(cv_embed, jd_embed))
