$('#addGoalModal').on('hidden.bs.modal', function () {
  $('#addGoalForm').trigger('reset');
});

  function changeImage(muscle) {
    var image = document.getElementById('muscle-img');
    if (muscle === 'chest') {
        image.src = '../static/workouts/CHESTT.png'; // Assuming your static files are served from '/static/'
    } else if(muscle=== 'back') {
        // Add image sources for other muscles if needed
        image.src = '../static/workouts/BACK.png';
    } else if(muscle=== 'glutes') {
      // Add image sources for other muscles if needed
      image.src = '../static/workouts/GLUTES.png';
    } else{
      image.src = '../static/workouts/MUSCLE.png';
    }
  }