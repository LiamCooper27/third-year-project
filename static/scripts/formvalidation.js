function fnValidateForm() {

	var errorMsg = "";

	var isEverythingOkay = true;

	var name = document.forms.testform.sendername.value;
	if (name.length < 2 || name.length > 40) {
		isEverythingOkay = false;
		errorMsg += '<p>*Name = Invalid data entered</p>';
	}

	var email = document.forms.testform.email.value;
	var atindex = email.indexOf("@");
	var dotindex = email.lastIndexOf(".");
	if (atindex < 1 || dotindex <= atindex) {
		isEverythingOkay = false;
		errorMsg += '<p>*Email = Invalid data entered</p>';
	}

	var message = document.forms.testform.message.value;
	if (message.length < 2) {
		isEverythingOkay = false;
		errorMsg += '<p>*Message = Invalid data entered</p>';
	}

	if (!isEverythingOkay) {
		document.getElementById("error").style.visibility = "visible";
		document.getElementById("error").style.display = "block";
		document.getElementById("error").innerHTML = errorMsg;
	}

	return isEverythingOkay;
}
