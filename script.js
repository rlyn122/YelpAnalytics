function showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.classList.add('hidden');
    });

    // Show the requested section
    const targetSection = document.getElementById(sectionId);
    targetSection.classList.remove('hidden');

    // Scroll to the top of the page instantly
    window.scrollTo({ top: 0, behavior: 'auto' });

    // Update progress bar
    updateProgressBar(sectionId);
}


function updateProgressBar(sectionId) {
    const progressBar = document.getElementById('progress-bar');
    let progressPercentage = 0;
    switch (sectionId) {
        case 'introduction':
            progressPercentage = 0;
            break;
        case 'Setup':
            progressPercentage = 10;
            break;
        case 'Dataset':
            progressPercentage = 20;
            break;
        case 'analysis1':
            progressPercentage = 40;
            break;
        case 'analysis2':
            progressPercentage = 60;
            break;
        case 'analysis3':
            progressPercentage = 80;
            break;
        case 'conclusion':
            progressPercentage = 100;
            break;
        default:
            progressPercentage = 0; // Resets or any other case
    }
    progressBar.style.width = progressPercentage + '%';
}
