def register_view_member(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save the user but deactivate him
            user = form.save(commit=False)
            user.type = User.Types.MEMBER
            form.save()
            messages.success(request, "Owner is created. login now.")
            return redirect("users:login_view")
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, "users/register-owner.html", context)
