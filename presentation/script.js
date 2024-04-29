function showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.classList.add('hidden');
    });

    // Show the requested section
    const targetSection = document.getElementById(sectionId);
    targetSection.classList.remove('hidden');
}
