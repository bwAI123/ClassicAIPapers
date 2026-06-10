import requests
import os

papers_arxiv = [
    "1409.1556", "1409.4842", "1512.03385", "1505.04597", "1502.03167",
    "1506.01497", "1506.02640", "1704.04861", "1905.11946",
    "1706.03762", "1810.04805", "1907.11692", "1910.10683", "2005.14165",
    "2103.00020", "2102.12092", "2201.12086", "2204.14198", "2304.08485", "2309.17421",
    "1406.2661", "1312.6114", "1812.04948", "2006.11239", "2112.10752", "2212.09748",
    "2010.11929", "2111.06377", "2002.05709", "1911.05722",
    "1312.5602", "1707.06347"
]

os.makedirs("papers", exist_ok=True)

for arxiv_id in papers_arxiv:
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with open(f"papers/{arxiv_id}.pdf", "wb") as f:
                f.write(r.content)
            print(f"✓ Downloaded {arxiv_id}")
        else:
            print(f"✗ Failed {arxiv_id}: {r.status_code}")
    except Exception as e:
        print(f"✗ Error {arxiv_id}: {e}")

