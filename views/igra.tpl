<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
</head>


<html>


<body>

  <h1>Vislice</h1>
  <h2>Igraš igro:</h2>
  <h3>Si v stanju {{ stanje }}</h3>

  <h3>Pravilni del gesla</h3>
  <h4>{{ igra.pravilni_del_gesla() }}</h4>

  <h3>Nepravilne črke</h3>
  <h4>{{ igra.napacne_crke() }}</h4>

  <h3>Stopnja obešenosti</h3>
  <h4>{{ igra.stevilo_napak() }}</h4>


  <img src="img/{{ igra.stevilo_napak() }}.jpg" alt="Stopnja obešenosti">

 <!-- Ker nas preusmeri na isto stran ni treba dati actiona -->
  <form method="POST">
    <label> Vnesi črko:
        <input type="text" name="crka">
    </label>
    <input type="submit">
  </form>



</body>

</html>