{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/e38213b91d3786389a446dfce4ff5a8aaf6012f2";
    devshell = {
      url = "github:deemp/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    flake-parts.url = "github:hercules-ci/flake-parts";
    systems.url = "github:nix-systems/default";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.devshell.flakeModule
      ];
      systems = import inputs.systems;
      perSystem =
        { pkgs, ... }:
        let
          python = pkgs.python3.withPackages (ps: [ ps.markdown-it-py ps.pydantic ]);
        in
        {
          devshells.default = {
            bash.extra = ''
              export ROOT_DIR="$(pwd)"
            '';
            commandGroups = {
              "1-front-tools" = [
                pkgs.nodejs_25
                pkgs.pnpm
              ];
              "2-back-tools" = [
                pkgs.uv
              ];
              "3-lint-tools" = [
                pkgs.lychee
              ];
              "4-instructors" = [
                {
                  name = "process-meeting-transcript";
                  command = ''
                    ${pkgs.lib.getExe python} ${./instructors/scripts/process-meeting-transcript/process-meeting-transcript.py} "$@"
                  '';
                  help = "Process a meeting transcript directory into speaker-labelled text files";
                }
                {
                  name = "find-broken-links";
                  command = ''
                    ${pkgs.lib.getExe pkgs.lychee} \
                      --include-fragments \
                      --offline \
                      --max-cache-age 0d \
                      --no-progress \
                      --exclude-path '.venv' \
                      --exclude-path '.uv-cache' \
                      --exclude-path '.direnv' \
                      --exclude-path 'node_modules' \
                      --exclude-path 'tmp' \
                      --exclude-path 'nanobot/packages' \
                      --root-dir . \
                      --format json \
                      "$ROOT_DIR"/'**/*.md' \
                      | ${pkgs.lib.getExe python} ${./instructors/scripts/find-broken-links/post-process-lychee.py}
                  '';
                  help = "Find all broken links in all Markdown files (with file:line locations)";
                }
                {
                  name = "lint-docs";
                  command = ''
                    ${pkgs.lib.getExe pkgs.markdownlint-cli2} \
                      '**/*.md' \
                      '#.direnv' \
                      '#**/.venv' \
                      '#**/.uv-cache' \
                      '#**/node_modules' \
                      '#*/skills' \
                      '#tmp' \
                      '#instructors/{file-reviews,meetings,scripts,lab-plan.md}' \
                      '#qwen-code-api' \
                      '#nanobot/packages'
                  '';
                  help = "Lint all Markdown files";
                }
              ];
            };
          };
        };
    };
}
