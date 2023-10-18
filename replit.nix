{ pkgs }: {
  deps = [
    pkgs.python39Packages.pip
    pkgs.cowsay
    pkgs.python39Packages.flask
  ];
}
