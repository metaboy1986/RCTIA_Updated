from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

advisories = [
    {"id": 1, "title": "Ransomware Targeting Healthcare", "date": "2025-07-01", "type": "Ransomware", "ref": "https://thehackernews.com"},
    {"id": 2, "title": "Worm spreading via SMB", "date": "2025-06-30", "type": "Worm", "ref": "https://bleepingcomputer.com"}
]

ioc_data = {
    "Worm": ["worm-ioc-1", "worm-ioc-2"],
    "Virus": ["virus-ioc-1"],
    "Trojan": ["trojan-ioc-1", "trojan-ioc-2", "trojan-ioc-3"]
}

@app.route('/')
def index():
    return render_template('index.html', advisories=advisories[:10], ioc_data=ioc_data)

@app.route('/ctia/all')
def ctia_all():
    return render_template('ctia_all.html', advisories=advisories)

@app.route('/ctia/<int:adv_id>')
def ctia_detail(adv_id):
    advisory = next((a for a in advisories if a["id"] == adv_id), None)
    return render_template('ctia_detail.html', advisory=advisory)

@app.route('/ioc/<ioc_type>')
def ioc_list(ioc_type):
    iocs = ioc_data.get(ioc_type, [])
    return render_template('ioc_list.html', iocs=iocs, ioc_type=ioc_type)

if __name__ == '__main__':
    app.run(debug=True)