from speedtest import Speedtest
st = Speedtest()
print(f"Tu velocidad de Descarga es: {st.download()}.");
print(f"Tu velocidad de Subida es: {st.upload()}.");
print(f"Tu Ping es: {st.results.ping}.");