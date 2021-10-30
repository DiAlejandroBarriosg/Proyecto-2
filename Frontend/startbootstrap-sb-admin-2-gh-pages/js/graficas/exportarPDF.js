var ctxBarChart = document.getElementById("myBarChart");
var ctxPieChart = document.getElementById("myPieChart");

function exportarBarrasPDF(){

    // Crear imagen de la grafica

    let imgCanvas = ctxBarChart.toDataURL("image/png", 1.0);

    // Crear PDF desde la imagen

    let documento = new jsPDF('landscape');
	documento.setFontSize(20);
	documento.text(15, 15, "Gráfica de barras");
    documento.setFillColor(204, 204,204,0);
	documento.addImage(imgCanvas, 'JPEG', 10, 25, 200, 150 );
	documento.save('graficaBarras.pdf');
}

function exportarPiePDF(){

    // Crear imagen de la grafica

    let imgCanvas = ctxPieChart.toDataURL("image/png", 1.0);

    // Crear PDF desde la imagen

    let documento = new jsPDF('landscape');
	documento.setFontSize(20);
	documento.text(15, 15, "Gráfica de pie");
    documento.setFillColor(204, 204,204,0);
	documento.addImage(imgCanvas, 'JPEG', 10, 25, 300, 150 );
	documento.save('graficaPie.pdf');
}
