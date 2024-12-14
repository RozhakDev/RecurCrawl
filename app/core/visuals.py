import os
from typing import Dict, Any
import matplotlib
import matplotlib.pyplot as plt
from flask import url_for

matplotlib.use('Agg')

class VisualizationService:
    """
    Kelas ini bertanggung jawab untuk membuat visualisasi data
    berdasarkan hasil analisis.
    """
    def __init__(self, analysis_results: Dict[str, Any]):
        self.results = analysis_results
        self.output_dir = os.path.join('app', 'static', 'images')
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _create_diagram(self) -> str:
        """Membuat dan menyimpan grafik perbandingan waktu eksekusi."""
        sizes = self.results["sizes"]
        iter_times = self.results["iterative_times"]
        rec_times = self.results["recursive_times"]
        
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, iter_times, marker='o', linestyle='-', label='Iteratif')
        plt.plot(sizes, rec_times, marker='x', linestyle='--', label='Rekursif')
        
        plt.title('Perbandingan Waktu Eksekusi: Iteratif vs. Rekursif', fontsize=16)
        plt.xlabel('Ukuran Dataset', fontsize=12)
        plt.ylabel('Waktu Eksekusi (detik)', fontsize=12)
        plt.grid(True, which="both", ls="--", linewidth=0.5)
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')
        
        filename = 'diagram.png'
        save_path = os.path.join(self.output_dir, filename)
        plt.savefig(save_path, bbox_inches='tight', dpi=100)
        plt.close()
        
        return url_for('static', filename=f'images/{filename}')
    
    def _create_table(self) -> str:
        """Membuat dan menyimpan tabel hasil sebagai gambar."""
        headers = ["Ukuran Data", "Waktu Iteratif (s)", "Waktu Rekursif (s)"]
        table_data = [
            (size, f"{it:.6f}", f"{rt:.6f}")
            for size, it, rt in zip(self.results["sizes"], self.results["iterative_times"], self.results["recursive_times"])
        ]
        
        fig, ax = plt.subplots(figsize=(8, 2))
        ax.axis('tight')
        ax.axis('off')
        
        table = ax.table(cellText=table_data, colLabels=headers, loc='center', cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)
        
        filename = 'tabel.png'
        save_path = os.path.join(self.output_dir, filename)
        plt.savefig(save_path, bbox_inches='tight', dpi=150)
        plt.close()
        
        return url_for('static', filename=f'images/{filename}')
    
    def generate_all_visuals(self) -> Dict[str, str]:
        """Menghasilkan semua visual (diagram dan tabel) dan mengembalikan path-nya."""
        diagram_path = self._create_diagram()
        table_path = self._create_table()
        
        return {
            "diagram_path": diagram_path,
            "tabel_path": table_path
        }