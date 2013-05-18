courseTemplate = ({code, name, professor}) ->
  """
  <div class='course-result'>
    <p class='course-result-code'>#{code}</p
    <p class='course-result-name'>#{name}</p>
    <p class='course-result-professor'>#{formatName professor}</p>
  </div>
  """

formatName = (name) ->
  [last, first] = name.split ','
  "#{first} #{last}"

updateCourseResults = (results) ->
  $("#course-results").html ''
  for result in results
    $("#course-results").append courseTemplate result

autocomplete = (term) ->
  # in lieu of the actual searching code
  [{code: "ARHA385", name: "European Architecture to 1750", professor: "Siry,Joseph M."},
  {code: "ARHA385", name: "European Architecture to 1750", professor: "Siry,Joseph M."},
  {code: "ARHA385", name: "European Architecture to 1750", professor: "Siry,Joseph M."},
  {code: "ARHA385", name: "European Architecture to 1750", professor: "Siry,Joseph M."}]

$ ->
  $("#course-search").on 'input', ->
    courseResults = autocomplete @value
    updateCourseResults courseResults

  window.theSchedule = new Schedule(window.theData, $('#schedule'))