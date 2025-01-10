document.addEventListener('DOMContentLoaded', function() {
    const bmiValueElement = document.getElementById('bmiValue');
    const kategoria = bmiValueElement.getAttribute('data-category');

    let color;
    switch (kategoria) {
        case 'Niedowaga':
            color = '#00FFFF';
            break;
        case 'Prawidłowa':
            color = '#5cb85c';
            break;
        case 'Nadwaga':
            color = '#f0ad4e';
            break;
        case 'Otyłość':
            color = '#d9534f';
            break;
        default:
            color = '#000000';
    }

    bmiValueElement.style.color = color;
});