import os
from flask import request, jsonify, render_template
from werkzeug.utils import secure_filename

from app import app
from app.core.analysis import AnalysisService
from app.core.visuals import VisualizationService

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename: str) -> bool:
    """Memvalidasi ekstensi file yang diizinkan."""
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    """Endpoint utama untuk menangani analisis algoritma."""
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        if 'json_file' not in request.files:
            return jsonify({'error': 'File JSON tidak ditemukan.'}), 400
    
    file = request.files['json_file']
    dataset_sizes_str = request.form.get('dataset_sizes')

    if file.filename == '' or not dataset_sizes_str:
        return jsonify({'error': 'File atau ukuran dataset tidak boleh kosong.'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Format file tidak valid, harus .json.'}), 400
    
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(filepath)

        sizes = [int(s.strip()) for s in dataset_sizes_str.split(',')]

        analysis_service = AnalysisService(filepath)
        results = analysis_service.run_comparison(sizes)

        visual_service = VisualizationService(results)
        output_paths = visual_service.generate_all_visuals()

        return jsonify(output_paths)
    except ValueError:
        return jsonify({'error': 'Ukuran dataset tidak valid. Masukkan angka dipisahkan koma.'}), 400
    except Exception as e:
        app.logger.error(f"Terjadi kesalahan internal: {e}")
        return jsonify({'error': f'Terjadi kesalahan pada server: {e}'}), 500

os.makedirs(UPLOAD_FOLDER, exist_ok=True)