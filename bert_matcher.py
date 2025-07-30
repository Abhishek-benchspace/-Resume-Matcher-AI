from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(resume_text, job_descriptions):
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    role_embs = model.encode(job_descriptions, convert_to_tensor=True)
    sims = util.cos_sim(resume_emb, role_embs)[0].cpu().numpy()
    return sims
