# -*- coding: utf-8 -*-
"""
Ejecución en Visual Studio Code con redirección automática de SALIDAS:
- Crea carpetas ./figuras y ./reportes si no existen.
- Redirige TODAS las gráficas generadas por matplotlib a ./figuras
  * Reemplaza plt.show() por guardado automático .png
  * Reescribe plt.savefig(...) para guardar SIEMPRE en ./figuras (conserva el nombre)
- Mantiene tu script original tal cual: solo lo importamos para que se ejecute.

Cómo usar:
1) Estructura recomendada del proyecto (coloca tus excels en /data):

   proyecto/
   ├─ data/
   │  ├─ base_datos_completa_NNA_TI_anon.xlsx
   │  └─ af_filtrado (1).xlsx
   ├─ figuras/
   ├─ reportes/
   ├─ copia_de_prueba_python.py   <-- tu script original (sin cambios)
   └─ main.py                     <-- este archivo

2) Ejecuta:
   $ python main.py

Notas:
- Si tu script original guarda tablas/Excel con rutas relativas, quedarán junto a main.py. 
  Si quieres forzar que TODO lo tabular vaya a ./reportes, puedes usar la función helper save_table(...)
  incluida abajo (opcional). Reemplaza tus .to_csv/.to_excel por save_table.
- No necesitamos editar tu lógica: este archivo sólo intercepta matplotlib.
"""
from __future__ import annotations
import os
from pathlib import Path
import datetime as _dt

# --------------------------------------------------------------------------------------
# 0) Paths base del proyecto
# --------------------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / "data"
FIG_DIR = ROOT_DIR / "figuras"
REP_DIR = ROOT_DIR / "reportes"

FIG_DIR.mkdir(parents=True, exist_ok=True)
REP_DIR.mkdir(parents=True, exist_ok=True)

# Fija el directorio de trabajo en la raíz del proyecto para rutas relativas
os.chdir(ROOT_DIR)

# --------------------------------------------------------------------------------------
# 1) Parcheo de matplotlib: todo show() y savefig() -> ./figuras
# --------------------------------------------------------------------------------------
import matplotlib
matplotlib.use("Agg")  # backend no-interactivo para guardado de archivos
import matplotlib.pyplot as plt

# Contador global para nombres automáticos de figuras
_auto_fig_counter = 1

def _auto_fig_path(fmt: str = "png", prefix: str = "fig") -> Path:
    global _auto_fig_counter
    fname = f"{prefix}_{_auto_fig_counter:03d}.{fmt}"
    _auto_fig_counter += 1
    return FIG_DIR / fname

# Guardamos referencia del savefig original
_original_savefig = plt.savefig


def _patched_savefig(fname=None, *args, **kwargs):
    """Parche para plt.savefig() que obliga a guardar en ./figuras.
    - Si el usuario pasa un nombre: usamos ese nombre pero movido a FIG_DIR.
    - Si no pasa nombre: generamos uno automático.
    """
    # Detectar formato deseado
    fmt = None
    if isinstance(fname, (str, os.PathLike)) and Path(fname).suffix:
        fmt = Path(fname).suffix.lstrip(".")
    if fmt is None:
        fmt = kwargs.get("format", "png")

    # Resolver nombre final dentro de FIG_DIR
    if fname is None:
        out_path = _auto_fig_path(fmt=fmt)
    else:
        name_only = Path(fname).name  # conserva el nombre original
        out_path = FIG_DIR / name_only

    out_path.parent.mkdir(parents=True, exist_ok=True)
    return _original_savefig(out_path, *args, **kwargs)


def _patched_show(*args, **kwargs):
    """Parche para plt.show(): en lugar de mostrar, guarda y cierra.
    - Genera nombre automático fig_XXX.png en ./figuras
    """
    fmt = kwargs.pop("format", "png")
    out_path = _auto_fig_path(fmt=fmt)
    _original_savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close("all")


# Aplicar parches
plt.savefig = _patched_savefig
plt.show = _patched_show

# Opcional: dirigir el directorio por defecto de guardado
plt.rcParams["savefig.directory"] = str(FIG_DIR)

# --------------------------------------------------------------------------------------
# 2) Helper opcional para REPORTES (tablas/archivos): save_table
# --------------------------------------------------------------------------------------
from typing import Optional, Union
try:
    import pandas as pd
except Exception:  # pragma: no cover
    pd = None  # Si no hay pandas, el helper seguirá permitiendo guardar binarios


def save_table(obj: "pd.DataFrame | pd.Series | bytes | str", 
               name: str,
               fmt: Optional[str] = None,
               index: bool = False,
               **to_kwargs):
    """Guarda un DataFrame/Series/bytes/texto dentro de ./reportes con nombre `name`.
    - Si `name` no tiene extensión y `fmt` es None, se asume .csv para DataFrame/Series y .txt para cadenas.
    - Ejemplos:
        save_table(df, "resumen")                -> ./reportes/resumen.csv
        save_table(df, "resumen.xlsx")           -> ./reportes/resumen.xlsx
        save_table("texto", "notas")             -> ./reportes/notas.txt
        save_table(b"bytes", "raw.bin")          -> ./reportes/raw.bin
    """
    out = Path(name)
    if not out.suffix:
        if fmt:
            out = out.with_suffix("." + fmt.lstrip("."))
        else:
            if pd is not None and (hasattr(obj, "to_csv") or hasattr(obj, "to_excel")):
                out = out.with_suffix(".csv")
            elif isinstance(obj, (str, bytes)):
                out = out.with_suffix(".txt")
            else:
                out = out.with_suffix(".out")

    out_path = REP_DIR / out.name
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if pd is not None and hasattr(obj, "to_excel") and out_path.suffix.lower() in {".xlsx", ".xls"}:
        obj.to_excel(out_path, index=index, **to_kwargs)
    elif pd is not None and hasattr(obj, "to_csv") and out_path.suffix.lower() in {".csv", ".tsv"}:
        if out_path.suffix.lower() == ".tsv":
            to_kwargs.setdefault("sep", "\t")
        obj.to_csv(out_path, index=index, **to_kwargs)
    elif isinstance(obj, str):
        out_path.write_text(obj, encoding="utf-8")
    elif isinstance(obj, bytes):
        out_path.write_bytes(obj)
    else:
        # Último recurso: str(obj)
        out_path.write_text(str(obj), encoding="utf-8")

    return out_path


# --------------------------------------------------------------------------------------
# 3) Variables de conveniencia para tus rutas de datos (si las usas)
#    *NO* obligatorias. Úsalas si quieres referenciar /data fácilmente.
# --------------------------------------------------------------------------------------
EXCEL_1 = DATA_DIR / "base_datos_completa_NNA_TI_anon.xlsx"
EXCEL_2 = DATA_DIR / "af_filtrado (1).xlsx"

# --------------------------------------------------------------------------------------
# 4) Ejecutar tu script original sin cambios
# --------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Importa y ejecuta el script existente. Si tu script tiene código al nivel superior,
    # se correrá al importar. Si define funciones con if __name__ == '__main__':, también se respetará.
    # Asegúrate de que el archivo "copia_de_prueba_python.py" esté en la raíz del proyecto (junto a main.py).
    try:
        import importlib
        # Si deseas forzar una recarga durante desarrollo: importlib.reload(module)
        import copia_de_prueba_python  # noqa: F401
    except ModuleNotFoundError as e:
        raise SystemExit(
            "No se encontró 'copia_de_prueba_python.py' junto a main.py. "
            "Coloca tu script original en la misma carpeta y vuelve a ejecutar."
        ) from e
    except Exception as e:
        # Superficialmente reportamos y dejamos traza mínima
        raise
