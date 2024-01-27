from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DefaultConfiguratorConfig:
    """
    This class configures `DefaultConfigurator`.
    """

    git_files_by_commit_id_url_prefix: str = field(default = 0)
    """
    Provides an URL prefix to access files by commit id.

    See also `AbstractConfigurator.provide_project_git_files_by_commit_id_url_prefix`.
    """

    commit_id_url_prefix: str = field(default = 0)
    """
    Provides an URL prefix to access page with commit id.

    See also `AbstractConfigurator.provide_project_commit_id_url_prefix`.
    """
