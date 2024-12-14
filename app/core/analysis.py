import json
import time
from typing import List, Dict, Any, Tuple

class AnalysisService:
    """
    Kelas ini bertanggung jawab untuk melakukan analisis perbandingan
    antara algoritma crawler iteratif dan rekursif.
    """
    def __init__(self, data_path: str):
        self.data = self._load_data(data_path)
    
    def _load_data(self, path: str) -> List[Dict[str, Any]]:
        """Memuat data JSON dari path file."""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _time_function(self, func, *args) -> float:
        """Mengukur waktu eksekusi sebuah fungsi."""
        start_time = time.time()
        func(*args)
        return time.time() - start_time
    
    def _iterative_crawler(self, size: int) -> None:
        """Implementasi crawler dengan pendekatan iteratif."""
        result = []
        stack = self.data[:size]
        while stack:
            current_post = stack.pop(0)
            result.append(current_post)
            if 'replies' in current_post:
                for reply in current_post['replies']:
                    stack.append(reply)
    
    def _recursive_crawler(self, size: int) -> None:
        """Implementasi crawler dengan pendekatan rekursif."""
        result = []
        def crawl(posts):
            for post in posts:
                result.append(post)
                if 'replies' in post:
                    crawl(post['replies'])
        crawl(self.data[:size])
    
    def run_comparison(self, dataset_sizes: List[int]) -> Dict[str, Any]:
        """
        Menjalankan perbandingan untuk beberapa ukuran dataset dan
        mengembalikan hasilnya dalam bentuk dictionary.
        """
        iterative_times = []
        recursive_times = []

        for size in dataset_sizes:
            iterative_time = self._time_function(self._iterative_crawler, size)
            recursive_time = self._time_function(self._recursive_crawler, size)
            iterative_times.append(iterative_time)
            recursive_times.append(recursive_time)
        
        return {
            "sizes": dataset_sizes,
            "iterative_times": iterative_times,
            "recursive_times": recursive_times
        }
