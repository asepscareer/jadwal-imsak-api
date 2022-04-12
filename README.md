API Jadwal Imsakiyah Indonesia ini dibuat menggunakan fastAPI. Semoga bisa digunakan, bermanfaat, dan semoga bisa berkontribusi untuk mengembangkan API ini, terimakasih.

## Penggunaan di local server
```bash
git clone https://github.com/asepscareer/jadwal-imsak-api.git
```

```bash
cd jadwal-imsak-api && pip install -r requirements.txt
```

```bash
uvicorn main:app --reload
```

# jadwal-imsak-api
kumpulan data jadwal imsak seluruh daerah di negara Indonesia.

### penggunaan

<table>
<thead>
<tr>
  <th>No</th>
  <th>Keterangan</th>
  <th>Endpoint</th>
  <th>Parameter</th>
  <th>Method</th>
</tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>Get Data Daerah</td>
    <td>/api/v1/get-daerah</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Get Data Imsak</td>
    <td>/api/v1/get-data</td>
    <td>Ada</td>
    <td>POST</td>
  </tr>
</tbody>
</table>

# Dokumentasi API
lokal -> http://127.0.0.1:8000/docs